'use client';

import { Input, Button } from '@nextui-org/react';
import Head from 'next/head';
import { useRouter } from 'next/navigation';
import { useState } from 'react';
import { FaRegEye, FaRegEyeSlash } from 'react-icons/fa';
import toast, { Toaster } from 'react-hot-toast';

export default function Login() {
	const router = useRouter();
	const [isVisible, setIsVisible] = useState(false);
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [isLoading, setIsLoading] = useState(false);

	const toggleVisibility = () => setIsVisible(!isVisible);
	const handleLogin = (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();

		if (!email || !password) {
			toast.error('Preencha todos os campos!');
			return;
		}

		setIsLoading(true);
		setTimeout(() => {
			setIsLoading(false);
			toast.success('Login efetuado com sucesso!');
			router.push('/dashboard');
		}, 2000);
	};

	return (
		<div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-gray-100 to-gray-300">
			<Toaster position="top-center" gutter={8} />
			<Head>
				<title>Login</title>
			</Head>
			<div className="mb-8">
				<img src="/logo.png" alt="Logo" className="w-80 h-80 object-contain" />
			</div>
			<div className="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full">
				<h2 className="text-2xl font-semibold text-center text-gray-700 mb-6">Presgen dashboard</h2>
				<form className="flex flex-col gap-6" onSubmit={handleLogin}>
					<Input type="email" label="Email" fullWidth className="text-lg" onChange={(e) => setEmail(e.target.value)} />
					<Input
						label="Senha"
						variant="bordered"
						endContent={
							<button className="focus:outline-none flex items-center" type="button" onClick={toggleVisibility} aria-label="toggle password visibility" style={{ height: '100%' }}>
								{isVisible ? <FaRegEye className="text-xl text-gray-500" /> : <FaRegEyeSlash className="text-xl text-gray-500" />}
							</button>
						}
						type={isVisible ? 'text' : 'password'}
						onChange={(e) => setPassword(e.target.value)}
						fullWidth
						className="text-lg"
					/>
					<Button type="submit" color="primary" className="w-full h-full py-3 text-lg font-semibold bg-zinc-700 hover:bg-zinc-800 transition duration-200 ease-in-out" isLoading={isLoading}>
						Entrar
					</Button>
				</form>
				<div className="mt-6 text-center">
					<a href="#" className="text-sm hover:underline text-gray-600">
						Esqueceu a senha?
					</a>
				</div>
			</div>
		</div>
	);
}
