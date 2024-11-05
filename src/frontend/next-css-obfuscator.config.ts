let seed = Math.random().toString(36).substring(7);
module.exports = {
	enable: true,
	mode: 'random',
	refreshClassConversionJson: false,
	allowExtensions: ['.jsx', '.tsx', '.js', '.ts', '.html', '.rsc'],
	generatorSeed: seed,
	blackListedFolderPaths: ['./.next/cache', /\.next\/server\/pages\/api/, /_document..*js/, /_app-.*/, /__.*/],
};
