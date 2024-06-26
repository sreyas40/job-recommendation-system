import './JobCard.css';
import Chip from '@mui/material/Chip';
import Stack from '@mui/material/Stack';
import { v4 as uuid } from 'uuid';
import IconButton from '@mui/material/IconButton';
import CorporateFareRoundedIcon from '@mui/icons-material/CorporateFareRounded';
export default function JobCard({ data, id, expandView, background, profilePictureStyle }) {
    const chips = [data.workStyle, data.workingDays, ...(data.skills.map(e => e.skill).slice(0, 2))]
    console.log(chips)
    return (
        <div className="card" onClick={() => expandView(data.id)} style={background}>
            <div className='card-div1'>
                <h1 className='card-h1'>{data.jobTitle}</h1>
                <p className='card-company-name-p'>{data.companyName}</p>
                <Stack className="card-tags" direction="row" spacing={1}>
                    {chips.map(e => {
                        return (<Chip key={uuid()} className="card-tags-child" label={e} size='small' />)
                    })}

                </Stack>
                <p className='card-salary'>{data.currency} {data.salary[0]}{data.salary[1]? <span>- {data.salary[1]}</span>: <></>} per month</p>
            </div>
            <div className='card-div2'>
                <div className='card-img-container qualification-card-image' style={profilePictureStyle}>
                    <IconButton disabled>
                        <CorporateFareRoundedIcon fontSize='large' />
                    </IconButton>
                </div>
                <p className='card-time-p'>{data.postDate}</p>
            </div>
        </div>
    )
}