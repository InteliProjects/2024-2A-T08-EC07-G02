export default {
	client: 'legacy/axios',
	input: 'http://localhost:3333/openapi.json',
	output: 'src/client',
	services: {
		asClass: true,
	},
	base: 'http://localhost:3333',
}
