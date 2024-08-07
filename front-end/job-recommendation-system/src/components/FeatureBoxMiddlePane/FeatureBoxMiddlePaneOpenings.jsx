import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import JobCard from '../JobCard/JobCard';
import { Button } from '@mui/material'
import { Link } from 'react-router-dom';
import {getStorage} from '../../storage/storage';
import { v4 as uuid } from 'uuid';
import './FeatureBoxMiddlePane.css';
export default function FeatureBoxMiddlePaneOpenings({data, childData}) {
    const demoInfo = { jobTitle: "Python Developer", companyName: "Google LLC",workStyle:"on-site",workingDays:"Monday-Friday", skills: ["python","javascript"], currency: "₹", salary: "50k", postDate: "13/9/23" };
    const DISPLAY_COUNT = 3;
    const COMPANY_USERNAME = data.companyUsername;
    const companyOpenings = (data?.vacancies.filter(e=>!e.closed) || []).slice(0,3);
    console.log("received middle pane", companyOpenings)
    
    
    
    return (
        <div className="feature-box feature-box-middle-pane" id="feature-box-middle-pane">
            <h4 className="feature-title">{data.title}</h4>
            
            <div className="feature-box-container">
            {Object.keys(companyOpenings).length?
            <>
            {Object.keys(companyOpenings).map((card) => (<JobCard key={uuid()} id={companyOpenings[card]["id"]}  data={{ ...companyOpenings[card], 'userType': "seeker" }} link={data.userType == "employer"?"/employer/review-applications": `/seeker/openings/${COMPANY_USERNAME || getStorage("guestUsername")}/${companyOpenings[card]["id"]}`} />)).slice(0,2)}
            <hr className="line-separator"/>
                <div className='see-openings-footer'>
                    <Link to={data.userType == "employer"?"/employer/review-applications": `/seeker/openings/${COMPANY_USERNAME || getStorage("guestUsername")}/all`} state={{user_id: data.user_id}}>
                        <a className="openings-redirect-button">See all openings<ArrowForwardIcon/></a>
                    </Link>
                </div>
            </>
            :
            <p className='openings-exception-msg'>The organisation doesn't have any job openings at the moment.</p>
        }
                 
            </div>
        </div>
    )
}