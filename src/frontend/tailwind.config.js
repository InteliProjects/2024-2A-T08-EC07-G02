const { nextui } = require('@nextui-org/theme');
module.exports = {
	content: ['./src/**/*.{js,ts,jsx,tsx}', './src/components/**/*.{js,ts,jsx,tsx}', './node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}'],
	theme: {
		extend: {},
	},
	variants: {
		extend: {},
	},
	darkMode: 'class',
	plugins: [
		nextui({
			themes: {
				light: {
					colors: {
						primary: {
							DEFAULT: '#222222',
							foreground: '#fff',
						},
						secondary: {
							DEFAULT: '#05084f',
							foreground: '#fff',
						},
						focus: '#222222',
					},
				},
				dark: {
					colors: {
						primary: {
							DEFAULT: '#222222',
							foreground: '#fff',
						},
						secondary: {
							DEFAULT: '#05084f',
							foreground: '#fff',
						},
						focus: '#222222',
					},
				},
			},
		}),
	],
};
