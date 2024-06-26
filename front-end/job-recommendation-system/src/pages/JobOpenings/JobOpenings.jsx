//import Filter from "../components/Filter";
//import StatsAI from "../components/StatsAI";
import "./JobOpenings.css";
import Filter from "../../components/Filter/Filter";
import OpeningsListBar from "../../components/OpeningsListBar/OpeningsListBar";
import JobCardExpanded from "../../components/JobCardExpanded/JobCardExpanded";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

export default function JobOpeningsSection() {
    const receivedData = useLocation();
    const userType = receivedData["pathname"].includes("employer")?"employer":"seeker";
    const userData = {'type': userType, 'skills': ['python', 'java', 'react', 'ai'], "appliedJobs": [1,2,5,6]}
    //console.log("received data",receivedData)
    //const [selectedEntry, setEntry] = useState(null);
    const [selectedEntry, setEntry] = useState(receivedData["state"]?receivedData.state.highlightedId || 0: 0);//userData is for knowing if employer or seeker and further passing it down to components
    //console.log("selected entry", selectedEntry);
    const [searchVal, setSearch] = useState("");
    //demoInfo is example vacancy profiles
    const demoInfo = [{ id: 0, jobTitle: "Python Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},
                      { id: 1, jobTitle: "Java Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Moscow', empType: 'Internship', exp: '1-5 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["java", "AI"]},
                      { id: 2, jobTitle: "Ruby Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Uganda', empType: 'Temporary', exp: 'Fresher', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["ruby", "AI", "Django"]},
                      { id: 3, jobTitle: "Golang Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Alaska', empType: 'Internship', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},
                      { id: 4, jobTitle: "Game Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Germany', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["react", "AI", "Django"]},
                      { id: 5, jobTitle: "Python Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},
                      { id: 6, jobTitle: "Java Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'Alaska', empType: 'Temporary', exp: 'Fresher', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["reactor", "AI", "Django"]},
                      { id: 7, jobTitle: "Ruby Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},
                      { id: 8, jobTitle: "Golang Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'India', empType: 'Internship', exp: '1-5 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},
                      { id: 9,jobTitle: "Game Developer", companyName: "Google LLC", tags: ["on-site", "software / IT", "Monday-Friday"], currency: "RS", salary: ["5000","10000"], postDate: "13/9/23" , location: 'London', empType: 'Full-time', exp: '5-10 years', jobDesc: "This is for demo purpose" ,jobReq:"This is for demo purpose",skills: ["python", "AI", "Django"]},]
    const [filterstat, setFilter] = useState(false);
    const [filterparam, setParam] = useState({});
    const filtered = demoInfo.filter(id => id["skills"].map((tag)=>(tag.toLowerCase().includes(searchVal.toLowerCase()))).filter(Boolean).length?id:false)
    const [selectedJobEntry,setJobEntry] = useState(demoInfo.filter(e=>(e["id"]===selectedEntry?e:false))[0]);
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
        const expEntry = demoInfo.filter(e=>(e["id"]===selection?e:false));
        setJobEntry(expEntry[0]);
        
    }
    
    //console.log("selected entry", selectedEntry);
    useEffect(()=>expJob(selectedEntry),[selectedEntry]);
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
            <div className="openings-left-side-bar">
            <OpeningsListBar data={filtered} userType={userType} chooseEntry={chooseEntry} searchBar={searchBar} preselectedEntry={selectedEntry} filterFunc={filterStateSet}/>
            </div>
            {filterstat?
            <div className="filter">
                <Filter title="Filter" passFilteredDataFn={filterDataSet}/>
            </div>
            :
            <>
            </>
            }
            
            <div className={`job-desc-box${filterstat?" blur":""}`}>
            {selectedEntry!=null && filtered.length!=0?<JobCardExpanded data={selectedJobEntry} userData={userData}/>:<></>}
            </div>
        </div>
    )
}