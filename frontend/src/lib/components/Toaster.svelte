<script lang="ts">
	import { getToasts } from '$lib/toast.svelte';

	const toasts = getToasts();
</script>

<div class="toast toast-top toast-end z-50">
	{#each toasts as t (t.id)}
		<div class="alert shadow-lg border-2 font-medium {t.type === 'success' ? 'alert-success' : 'alert-error'}">
			<span>{t.message}</span>
		</div>
	{/each}
</div>
