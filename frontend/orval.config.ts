import { defineConfig } from 'orval';

export default defineConfig({
	default: {
		input: {
			target: 'http://localhost:8000/openapi.json'
		},
		output: {
			client: 'fetch',
			baseUrl: 'http://localhost:8000',
			target: './src/lib/api/gen',
			schemas: './src/lib/api/gen/model',
			mode: 'tags',
			clean: true
		}
	}
});
