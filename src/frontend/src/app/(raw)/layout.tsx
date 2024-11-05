import type { ReactElement, ReactNode } from 'react';
import '@styles/globals.scss';

export default function Layout({ children }: { children: ReactNode }): ReactElement {
	return (
		<html lang="pt-br">
			<body>
				<main>{children}</main>
			</body>
		</html>
	);
}
