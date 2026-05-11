<script lang="ts">
	import { invalidate } from '$app/navigation';
	import { patchTodo, deleteTodo } from '$lib/api/gen/todos';
	import type { Todo } from '$lib/api/gen/model';
	import { toast } from '$lib/toast.svelte';

	let { todo }: { todo: Todo } = $props();

	let toggling = $state(false);
	let deleting = $state(false);
	let editing = $state(false);
	let editTitle = $state('');
	let renaming = $state(false);
	let editInput = $state<HTMLInputElement | null>(null);

	$effect(() => { if (editInput) editInput.focus(); });

	async function handleToggle() {
		toggling = true;
		try {
			const { status } = await patchTodo(todo.id, { completed: !todo.completed });
			if (status === 200) {
				await invalidate('app:todos');
			} else {
				toast.error('Could not update todo');
			}
		} catch {
			toast.error('Network error. Try again.');
		} finally {
			toggling = false;
		}
	}

	async function handleDelete() {
		if (!confirm(`Delete "${todo.title}"?`)) return;
		deleting = true;
		try {
			const { status } = await deleteTodo(todo.id);
			if (status === 204) {
				toast.success('Todo deleted');
				await invalidate('app:todos');
			} else {
				toast.error('Could not delete todo');
			}
		} catch {
			toast.error('Network error. Try again.');
		} finally {
			deleting = false;
		}
	}

	function startEdit() {
		editing = true;
		editTitle = todo.title;
	}

	function cancelEdit() {
		editing = false;
		editTitle = '';
	}

	async function handleRename() {
		const title = editTitle.trim();
		if (!title || title === todo.title) { cancelEdit(); return; }
		editing = false;
		renaming = true;
		try {
			const { status } = await patchTodo(todo.id, { title });
			if (status === 200) {
				await invalidate('app:todos');
			} else {
				toast.error('Could not rename todo');
			}
		} catch {
			toast.error('Network error. Try again.');
		} finally {
			renaming = false;
			editTitle = '';
		}
	}
</script>

<li class="flex items-center gap-2">
	<input
		type="checkbox"
		class="checkbox"
		checked={todo.completed}
		disabled={toggling}
		onchange={handleToggle}
	/>
	{#if editing}
		<input
			class="input input-bordered input-sm flex-1"
			bind:value={editTitle}
			bind:this={editInput}
			onkeydown={(e) => {
				if (e.key === 'Enter') handleRename();
				if (e.key === 'Escape') cancelEdit();
			}}
		/>
	{:else}
		<span
			class="flex-1 cursor-pointer {todo.completed ? 'text-base-content/50 line-through' : ''}"
			onclick={startEdit}
			role="button"
			tabindex="0"
			onkeydown={(e) => e.key === 'Enter' && startEdit()}
		>
			{renaming ? '...' : todo.title}
		</span>
	{/if}
	<button
		class="btn btn-ghost btn-sm"
		disabled={deleting}
		onclick={handleDelete}
	>
		{deleting ? '...' : '✕'}
	</button>
</li>
