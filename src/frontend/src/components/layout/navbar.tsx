'use client';
import React, { ReactNode } from 'react';
import { Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Dropdown, DropdownItem, DropdownTrigger, DropdownMenu, Avatar } from '@nextui-org/react';
import { FaTachometerAlt, FaChartLine, FaCog } from 'react-icons/fa';
import { usePathname } from 'next/navigation';
import { Toaster } from 'react-hot-toast';
export function NavbarLayout({ children }: { children: ReactNode }) {
	const pathname = usePathname();

	const getLinkClass = (path: string) => {
		return pathname === path
			? 'text-blue-700 font-semibold text-xl transition-colors flex items-center'
			: 'text-gray-700 hover:text-blue-700 font-semibold text-xl transition-colors flex items-center';
	};

	return (
		<>
			<Toaster position="bottom-center" gutter={8} />
			<Navbar isBordered position="sticky" className="bg-white border-b border-gray-200 shadow-md py-4 px-6">
				<NavbarBrand>
					<Link href="/dashboard" className="flex items-center">
						<img src="/logo.png" alt="Logo" className="h-16 w-auto" />
					</Link>
				</NavbarBrand>

				<NavbarContent className="hidden sm:flex gap-8" justify="center">
					<NavbarItem>
						<Link href="/dashboard" color="foreground" className={getLinkClass('/dashboard')}>
							<FaTachometerAlt className="mr-2" />
							Dashboard
						</Link>
					</NavbarItem>
					<NavbarItem>
						<Link href="/predict" color="foreground" className={getLinkClass('/predict')}>
							<FaChartLine className="mr-2" />
							Predict
						</Link>
					</NavbarItem>
					<NavbarItem>
						<Link href="/advanced" color="foreground" className={getLinkClass('/advanced')}>
							<FaCog className="mr-2" />
							Avançado
						</Link>
					</NavbarItem>
				</NavbarContent>

				<NavbarContent as="div" justify="end">
					<Dropdown placement="bottom-end">
						<DropdownTrigger>
							<Avatar isBordered as="button" className="transition-transform" color="primary" size="lg" src="https://ui-avatars.com/api/?name=Vinicios+Lugli" />
						</DropdownTrigger>
						<DropdownMenu aria-label="User menu" variant="flat" disabledKeys={['profile']}>
							<DropdownItem key="profile" className="h-14 gap-2">
								<p className="font-semibold">Olá</p>
								<p className="font-semibold">vinicios@example.com</p>
							</DropdownItem>
							<DropdownItem key="settings">Configurações</DropdownItem>
							<DropdownItem key="logout" color="danger" href="/login">
								Sair
							</DropdownItem>
						</DropdownMenu>
					</Dropdown>
				</NavbarContent>
			</Navbar>

			<div className="flex-grow p-4">{children}</div>
		</>
	);
}
