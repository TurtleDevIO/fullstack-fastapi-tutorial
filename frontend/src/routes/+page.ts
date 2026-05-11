import { getTodos } from '$lib/api/gen/todos';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ depends }) => {
	depends('app:todos');
	return { todos: getTodos().then((r) => r.data) };
};
