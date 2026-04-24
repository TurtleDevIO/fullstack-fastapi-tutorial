<script lang="ts">
	import { getTodos } from '$lib/api/gen/todos';
	import type { Todo } from '$lib/api/gen/model';

	let todos = $state<Todo[]>([]);
	let loading = $state(false);
	let error = $state<string | null>(null);

	async function fetchTodos() {
		loading = true;
		error = null;
		try {
			const { data, status } = await getTodos();
			if (status === 200) {
				todos = data;
			} else {
				error = `Unexpected response: ${status}`;
			}
		} catch (e) {
			error = 'Failed to fetch todos. Is the backend running?';
		} finally {
			loading = false;
		}
	}
</script>

<div class="mx-auto mt-16 max-w-md px-4">
	<h1 class="mb-6 text-2xl font-bold">Todo App</h1>

	<button class="btn w-full btn-primary" onclick={fetchTodos} disabled={loading}>
		{loading ? 'Loading...' : 'Fetch Todos'}
	</button>

	{#if error}
		<div class="mt-4 alert text-sm alert-error">{error}</div>
	{/if}

	{#if todos.length > 0}
		<ul class="mt-4 space-y-2">
			{#each todos as todo}
				<li class="flex items-center gap-2">
					<span class="badge {todo.completed ? 'badge-success' : 'badge-ghost'}">
						{todo.completed ? '✓' : '○'}
					</span>
					{todo.title}
				</li>
			{/each}
		</ul>
	{:else if !loading}
		<p class="mt-4 text-center text-sm text-base-content/50">No todos yet.</p>
	{/if}
</div>
