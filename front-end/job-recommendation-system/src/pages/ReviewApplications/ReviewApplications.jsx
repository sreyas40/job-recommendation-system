//import Filter from "../components/Filter";
//import StatsAI from "../components/StatsAI";
import "./ReviewApplications.css";
import {getStorage} from "../../storage/storage";
import Filter from "../../components/Filter/Filter";
import OpeningsListBar from "../../components/OpeningsListBar/OpeningsListBar";
import JobDesciptionForm from "../../components/JobDescription/JobDesciption";
import BackBtn from "../../components/BackBtn/BackBtn";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import CandidateCard from "../../components/CandidateCard/CandidateCard";
import { set } from "react-hook-form";
import { jobAPI, userAPI } from "../../api/axios";

export default function ReviewApplications() {
    const receivedData = useLocation();
    const userType = receivedData["pathname"].includes("employer")?"employer":"seeker";
    const userData = {'type': userType, 'skills': ['python', 'java', 'react', 'ai'], "appliedJobs": []}
    //console.log("received data",receivedData)
    //const [selectedEntry, setEntry] = useState(null);
    const [selectedEntry, setEntry] = useState(receivedData["state"]?receivedData.state.highlightedId || null: null);//userData is for knowing if employer or seeker and further passing it down to components
    //console.log("selected entry", selectedEntry);
    const [searchVal, setSearch] = useState("");
    //demoInfo is example vacancy profiles
    const [jobVacancies, setJobVacancies] = useState([]);
    const [jobApplicants, setApplicants] = useState([]);
    /*const demoInfo = [{ },
                      { id: 1, jobTitle: "Java Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Moscow', empType: 'Internship', exp: '1-5 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["java", "AI"], applicationsReceived: [1,2,3,4,5,7,8,9]},
                      { id: 2, jobTitle: "Ruby Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Uganda', empType: 'Temporary', exp: 'Fresher', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["ruby", "AI", "Django"], applicationsReceived: [1,2,3,4,5,7,9]},
                      { id: 3, jobTitle: "Golang Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Alaska', empType: 'Internship', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"], applicationsReceived: [1,2,3,4,9]},
                      { id: 4, jobTitle: "Game Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Germany', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["react", "AI", "Django"], applicationsReceived: [1,2,3,4,5,]},
                      { id: 5, jobTitle: "Python Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"], applicationsReceived: [1,4,5,7,8,9]},
                      { id: 6, jobTitle: "Java Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Alaska', empType: 'Temporary', exp: 'Fresher', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["reactor", "AI", "Django"], applicationsReceived: [1,2,8,9]},
                      { id: 7, jobTitle: "Ruby Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"], applicationsReceived: [1,3,8,9]},
                      { id: 8, jobTitle: "Golang Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'India', empType: 'Internship', exp: '1-5 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"], applicationsReceived: [1,2,9]},
                      { id: 9,jobTitle: "Game Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"], applicationsReceived: [1,5,7,8,9]},]
    const profileInfo = [{ applicantID: 1,candidateName: "Amy Williams", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 2,candidateName: "Galvin Serie", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 3,candidateName: "Cole Nicol", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 4,candidateName: "Salvin Drone", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 5,candidateName: "Sepen Zen", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 6,candidateName: "Zeke John", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 7,candidateName: "Keire Helen", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 8,candidateName: "Karen Laneb", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2},
                      { applicantID: 9,candidateName: "Javan Dille", location: "Kerala, India", tags: ["on-site", "software / IT", "Monday-Friday"], experience:2} 
                    ];*/


    
    const [filterstat, setFilter] = useState(false);
    const [filterparam, setParam] = useState({});
    const filtered = (jobVacancies.length!=0?jobVacancies.filter(id => id["skills"].map((tag)=>(tag["skill"].toLowerCase().includes(searchVal.toLowerCase()))).filter(Boolean).length?id:false):[]);
    
    //const filtered = []
    const [selectedJobEntry,setJobEntry] = useState(null);
    //const [filteredApplicants, setfilteredApplicants]=useState(profileInfo.filter(applicants=>(selectedJobEntry["applicationsReceived"].includes(applicants["applicantID"])?applicants:false)));
    const [sidebarState, setSideBar] = useState(false);
    const callJobVacancyAPI= async (companyId)=>{
        try {
            const response = await jobAPI.get(`/job_vacancy/company/${companyId}`);
            const mod_response = response.data.map(e=>({id: e.job_id, jobTitle: e.job_name, companyName: e.company_name, tags: e.tags, currency: e.salary.split('-')[0], salary: [e.salary.split('-')[1],e.salary.split('-')[2]], postDate: e.created_at.split('T')[0] , location: e.location, empType: e.emp_type, exp: e.experience, jobDesc: e.job_desc ,jobReq:e.requirement,skills: e.skills, applicationsReceived: e.job_seekers}))
            setJobVacancies(mod_response);
            console.log(response);
            console.log("job vacancies", mod_response);
            console.log("filtered", filtered);
        } catch (e) {
            console.log("jobs failed", e)
            
            alert(e.message);
        }
    }
    const CreateJobRequest= async (jobId)=>{
        try {
            const response = await jobAPI.post('/job_request', {"job_id": jobId},
                {
                headers:{
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${getStorage("userToken")}`
                }         
                }
            );
            console.log("successfully created job request");
            console.log(response);
            
        } catch (e) {
            console.log("jobs failed", e)
            
            alert(e.message);
        }
    }

    const RequestJobApplications= async (applicantList)=>{
        
        try {
            const response = await userAPI.post('/seeker/details/list', {"user_ids": applicantList}, {
                headers:{
                    'Content-Type': 'application/json'
                }         
                });
            const mod_response = response.data.map(e=>({applicantID: e.user_id,candidateName: (e.first_name + " " + e.last_name), location: e.location, experience: e.experience}))
            setApplicants(mod_response);
            console.log("applicants receiveed", mod_response);
            
        } catch (e) {
            
            console.log("applicants failed", e)
            
            alert(e.message);
        }
    }
        
    console.log("applicants confirmed", jobApplicants)
    //console.log("sidebar", sidebarState)
    //console.log("filtered", filtered);
    const filterStateSet=(fstate)=>{
        setFilter(fstate);
    }
    const filterDataSet=(fdata)=>{
        setParam({...fdata});
    }
    //console.log("filter parameters", filterparam);
    const chooseEntry =(entry)=>{
        //function for passing selected job opening card from child component to parent componenet
        setEntry(entry);
    }

    const searchBar =(searchValue)=>{
        setSearch(searchValue);
    }
    const expJob=(selection)=>{
        //console.log("select", selection);
        const expEntry = jobVacancies.filter(e=>(e["id"]===selection?e:false));
        setJobEntry(expEntry[0]);
        RequestJobApplications(expEntry[0].applicationsReceived);
        console.log("selected entry: ", selectedEntry, " selected job: ", selectedJobEntry);
    }
    
    const listToDescParentFunc=()=>{
        setSideBar(true);
    }
    //console.log("filtered applicants",filteredApplicants);
    useEffect(() => {callJobVacancyAPI(23)}, []);//only runs during initial render
    useEffect(()=>{if(selectedEntry==null)
        {setEntry(jobVacancies[0]?jobVacancies[0].id:null)
         setJobEntry(jobVacancies[0]?jobVacancies[0]:null)
        }},[jobVacancies])
    useEffect(()=>{if(jobVacancies.length!=0 && selectedEntry!=null)expJob(selectedEntry)},[selectedEntry]);
    
    /*const resultGen=()=>{
        
            let result = demoInfo.filter(id => id["skills"].map((tag)=>(tag.includes(searchVal))).filter(Boolean).length?id:false)
            //console.log(result)
            setFilter(result);
        
        
        //console.log(typeof(searchVal))
        

    }
    useEffect(() => resultGen, [searchVal])
    */
    //console.log(`search=${searchVal}`);
    //console.log(filtered)
    //const result = demoInfo.filter((profiles) => profiles["tags"].map((tag)=>(tag.includes(searchVal))).filter(Boolean).length?profiles:null)
    //console.log(result)
    //const tags = [{"skills": ["hello", "hil", "how"]}, {"skills": ["helo", "hi", "how"]}, {"skills": ["kioo", "ka", "how"]},]
    //const newtags = tags.filter(id => id["skills"].map((tag)=>(tag.includes(searchVal))).filter(Boolean).length?id:false)
    //console.log(newtags)
    //console.log(searchVal);

    
    //console.log(`search=${searchVal}`);
   
    return (
        <div id="page">
            <div className={`review-left-bar${sidebarState?" wide":""}`}>
                {sidebarState?
                <>
                <JobDesciptionForm data={selectedJobEntry} userData={userData}/>
                <div className="back-button-review" onClick={()=>setSideBar(false)}><BackBtn outlineShape={"square"} butColor={"white"}/></div>
                </>
                :
                <OpeningsListBar data={filtered} userType={userType} pageType="review" chooseEntry={chooseEntry} searchBar={searchBar} listToDescParentFunc={listToDescParentFunc} preselectedEntry={selectedEntry} filterFunc={filterStateSet}/>
                }
            </div>
            {filterstat?
            <div className="filter enabled">
                <Filter title="Filter" passFilteredDataFn={filterDataSet}/>
            </div>
            :
            <></>
            }
            
            <div className={`applications-box${filterstat?" blur":""}${sidebarState?" wide":""}`}>
            {userType=="employer"?
                (selectedEntry!=null && filtered.length!=0 && jobApplicants.length!=0?
                    
                    jobApplicants.map(e=><CandidateCard type="review" data={e}/>)
                    :
                    <></>
                )
                :
                (selectedEntry!=null && filtered.length!=0?
                    <JobDesciptionForm data={selectedJobEntry} createJobRequest={CreateJobRequest} userData={userData}/>
                    :
                    <></>
                )
            }
            {}
            </div>
        </div>
    )
}