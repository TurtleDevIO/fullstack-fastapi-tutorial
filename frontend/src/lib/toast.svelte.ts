type Toast = { id: number; type: 'success' | 'error'; message: string };

let nextId = 0;
const toasts = $state<Toast[]>([]);

function show(type: Toast['type'], message: string) {
	const id = nextId++;
	toasts.push({ id, type, message });
	setTimeout(() => {
		const i = toasts.findIndex((t) => t.id === id);
		if (i !== -1) toasts.splice(i, 1);
	}, 4000);
}

export function getToasts() {
	return toasts;
}

export const toast = {
	success: (message: string) => show('success', message),
	error: (message: string) => show('error', message)
};
