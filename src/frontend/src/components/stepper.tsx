'use client';
import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import { ReactNode } from 'react';
import { StepIconProps } from '@mui/material/StepIcon';
import StepConnector, { stepConnectorClasses } from '@mui/material/StepConnector';
import { Typography } from '@mui/material';
import { styled, keyframes } from '@mui/material/styles';
import { Tooltip } from '@nextui-org/react';
import Fade from '@mui/material/Fade';

export interface StepDetail {
	name: string;
	icon: React.ReactElement<any>;
	error?: string | null;
	description?: string;
	tooltip?: string;
}

interface CustomStepperProps {
	steps: StepDetail[];
	currentStep: number;
	onStepChange?: (step: number) => void;
}

const slideAnimation = keyframes`
  0% {
    width: 0;
  }
  100% {
    width: 100%;
  }
`;

const rippleAnimation = keyframes`
  0% {
    transform: scale(0.8);
    opacity: 0.7;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
`;

const CustomStepIconRoot = styled('div')<{
	ownerState: { completed?: boolean; active?: boolean; error?: boolean };
}>(({ theme, ownerState }) => ({
	backgroundColor: ownerState.error && ownerState.active ? 'rgb(255,77,77)' : ownerState.active || ownerState.completed ? theme.palette.primary.main : theme.palette.grey[400],
	zIndex: 1,
	color: '#fff',
	width: 50,
	height: 50,
	display: 'flex',
	borderRadius: '50%',
	justifyContent: 'center',
	alignItems: 'center',
	boxShadow: ownerState.active ? '0 4px 10px 0 rgba(0,0,0,.25)' : 'none',
	backgroundImage:
		ownerState.error && ownerState.active
			? 'linear-gradient(136deg, rgb(255,77,77) 0%, rgb(255,0,0) 50%, rgb(180,0,0) 100%)'
			: ownerState.active || ownerState.completed
			? `linear-gradient(136deg, ${theme.palette.primary.light} 0%, ${theme.palette.primary.main} 50%, ${theme.palette.primary.dark} 100%)`
			: 'none',
	animation: ownerState.active ? `${rippleAnimation} 0.2s ease-in-out 0.2s` : 'none',
}));

const CustomConnector = styled(StepConnector)(({ theme }) => ({
	[`&.${stepConnectorClasses.alternativeLabel}`]: {
		top: 22,
		zIndex: -1,
	},
	[`&.${stepConnectorClasses.active}`]: {
		[`& .${stepConnectorClasses.line}`]: {
			backgroundImage: `linear-gradient(95deg, ${theme.palette.primary.light} 0%, ${theme.palette.primary.main} 50%, ${theme.palette.primary.dark} 100%)`,
			animation: `${slideAnimation} 0.2s ease-in-out`,
			zIndex: -1,
		},
	},
	[`&.${stepConnectorClasses.completed}`]: {
		[`& .${stepConnectorClasses.line}`]: {
			backgroundImage: `linear-gradient(95deg, ${theme.palette.primary.light} 0%, ${theme.palette.primary.main} 50%, ${theme.palette.primary.dark} 100%)`,
			zIndex: -1,
		},
	},
	[`& .${stepConnectorClasses.line}`]: {
		height: 3,
		border: 0,
		backgroundColor: theme.palette.grey[300],
		borderRadius: 1,
		zIndex: -1,
		...(theme.palette.mode === 'dark' && {
			backgroundColor: theme.palette.grey[700],
		}),
	},
}));

function CustomStepIcon(props: StepIconProps) {
	const { active, completed, className, error, icon } = props;

	return (
		<CustomStepIconRoot ownerState={{ completed, active, error }} className={className}>
			{icon}
		</CustomStepIconRoot>
	);
}

export function CustomStepper({ steps, currentStep, onStepChange }: CustomStepperProps) {
	return (
		<Box sx={{ width: '100%' }}>
			<Stepper activeStep={currentStep} alternativeLabel connector={<CustomConnector />}>
				{steps.map((step, index) => {
					const labelProps: {
						optional?: ReactNode;
						error?: boolean;
					} = {};

					const isCurrentStep = currentStep === index;

					if (step.error && isCurrentStep) {
						labelProps.optional = (
							<Fade in={isCurrentStep} easing="ease-in-out">
								<Typography variant="caption" color="error">
									{step.error}
								</Typography>
							</Fade>
						);
						labelProps.error = true;
					} else if (step.description && isCurrentStep) {
						labelProps.optional = (
							<Fade in={isCurrentStep}>
								<Typography variant="caption" color="textSecondary">
									{step.description}
								</Typography>
							</Fade>
						);
					}

					return (
						<Step key={step.name}>
							<StepLabel
								{...labelProps}
								StepIconComponent={(stepProps) => (
									<Tooltip content={step.tooltip || ''} color="primary" showArrow isDisabled={!step.tooltip}>
										<span>
											<CustomStepIcon {...stepProps} icon={step.icon} error={!!step.error} />
										</span>
									</Tooltip>
								)}
							>
								{step.name}
							</StepLabel>
						</Step>
					);
				})}
			</Stepper>
		</Box>
	);
}
