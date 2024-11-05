'use client';
import React, { ReactNode } from 'react';
import { NavbarLayout } from './navbar';

export function BaseLayout({ children }: { children: ReactNode }) {
	return <NavbarLayout>{children}</NavbarLayout>;
}
