<script lang="ts">
	import { invalidate } from '$app/navigation';
	import { createTodo } from '$lib/api/gen/todos';
	import { toast } from '$lib/toast.svelte';
	import TodoItem from '$lib/components/TodoItem.svelte';

	let { data } = $props();

	let newTitle = $state('');
	let creating = $state(false); // disables the button while the request is in flight

	async function handleCreate(e: SubmitEvent) {
		e.preventDefault();
		const title = newTitle.trim();
		if (!title || creating) return;
		creating = true;
		try {
			const { status } = await createTodo({ title });
			if (status === 201) {
				newTitle = '';
				toast.success('Todo added');
				await invalidate('app:todos');
			} else {
				toast.error('Could not add todo');
			}
		} catch {
			toast.error('Network error. Try again.');
		} finally {
			creating = false;
		}
	}
</script>

<div class="mx-auto mt-16 max-w-md px-4">
	<h1 class="mb-1 text-2xl font-bold">Todos</h1>
	<p class="mb-6 text-sm text-base-content/50">
		Every request has a 1s delay. Mutations (create, toggle, delete) have a ~20% chance of failing
		— so you can see the skeleton, the disabled button, and the error toast in action.
	</p>

	<form onsubmit={handleCreate} class="mb-6 flex gap-2">
		<input
			type="text"
			class="input input-bordered flex-1"
			placeholder="What needs doing?"
			bind:value={newTitle}
			disabled={creating}
		/>
		<button class="btn btn-primary" type="submit" disabled={creating || !newTitle.trim()}>
			{creating ? 'Adding...' : 'Add'}
		</button>
	</form>

	{#await data.todos}
		<div class="space-y-2">
			<div class="skeleton h-10 w-full"></div>
			<div class="skeleton h-10 w-full"></div>
			<div class="skeleton h-10 w-full"></div>
		</div>
	{:then todos}
		{#if todos.length === 0}
			<p class="text-center text-sm text-base-content/50">No todos yet.</p>
		{:else}
			<ul class="space-y-2">
				{#each todos as todo (todo.id)}
					<TodoItem {todo} />
				{/each}
			</ul>
		{/if}
	{:catch}
		<div class="alert alert-error">
			<span class="text-sm">Could not load todos. Is the backend running?</span>
		</div>
	{/await}
</div>
