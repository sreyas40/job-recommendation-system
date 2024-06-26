import { useForm } from 'react-hook-form';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import CheckRoundedIcon from '@mui/icons-material/CheckRounded';
import CloseRoundedIcon from '@mui/icons-material/CloseRounded';
import './QualificationAdd.css';
export default function QualificationAdd({ submitFn, cancelFn }) {
    const { register, formState: { errors }, handleSubmit } = useForm({ mode: 'onTouched' });

    return (

        <form className='qualification-add-form qualification-card' noValidate autoComplete='on' onSubmit={handleSubmit(submitFn)}>
            <div className="qualification-card-image"></div>
            <div className="qualification-card-content">
                <TextField sx={{ marginBottom: '.7rem' }} className='qualification-add-h2'
                    label="Course/Degree"
                    variant="outlined"
                    placeholder="Ex: B.Tech in Electronics"
                    InputLabelProps={{ shrink: true }}
                    size='small'
                    error={'education_title' in errors}
                    {...register("education_title", {
                        required: "qualification cannot be empty"
                    })} />
                <TextField sx={{ marginBottom: '.7rem' }} className='qualification-add-h3'
                    placeholder="Ex: Harvard University"
                    variant="outlined"
                    label="School/College"
                    InputLabelProps={{ shrink: true }}
                    size='small'
                    error={'education_provider' in errors}
                    {...register("education_provider", {
                        required: "qualification provider cannot be empty"
                    })} />
                <div className='qualification-year'>
                    <TextField className='qualification-add-p'
                        placeholder="2000"
                        variant="outlined"
                        label="Start year"
                        InputLabelProps={{ shrink: true }}
                        size='small'
                        error={'start_year' in errors}
                        {...register("start_year", {
                            required: "cannot be empty"
                        })} />
                    <p>-</p>
                    <TextField className='qualification-add-p'
                        placeholder="2010"
                        variant="outlined"
                        label="End year"
                        InputLabelProps={{ shrink: true }}
                        size='small'
                        error={'end_year' in errors}
                        {...register("end_year", {
                            required: "cannot be empty"
                        })} />
                </div>

            </div>
            <div className="qualification-card-action-btns">
                <Stack direction="column" spacing={2}>
                    <IconButton aria-label="edit" type='submit'>
                        <CheckRoundedIcon fontSize='small' />
                    </IconButton>
                    <IconButton aria-label="edit" onClick={() => { cancelFn() }}>
                        <CloseRoundedIcon sx={{ color: 'red' }} fontSize='small' />
                    </IconButton>
                </Stack>
            </div>
        </form>

    )
}