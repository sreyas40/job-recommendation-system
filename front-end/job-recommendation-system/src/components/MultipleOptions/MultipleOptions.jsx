import './MultipleOptions.css';
import FormGroup from '@mui/material/FormGroup';
import { Box } from '@mui/material';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import CheckCircleRoundedIcon from '@mui/icons-material/CheckCircleRounded';
import RadioButtonUncheckedRoundedIcon from '@mui/icons-material/RadioButtonUncheckedRounded';
import { v4 as uuid } from 'uuid';
import { useState, useEffect } from 'react';


export default function MultipleOptions({ heading, options, onChange=() => {}, preselected=null, dataType=null, checkLimit=1, fSize=".938rem", margY="15px"}) {
    const [checkedItems, setCheckedItems] = useState(preselected?{[preselected]: true}:{});
    const [update, setUpdate] = useState(false);
    //console.log(checkedItems)

    //function to handle changed check boxes way it 
    function handleChange(option){
        const updatedCheckedItems = {...checkedItems, [option]: !checkedItems[option]}
        setCheckedItems(updatedCheckedItems);
        setUpdate(true);
        
    }
    useEffect(()=>{if(update == true){onChange(checkedItems, checkLimit, dataType);
                                      setUpdate(false);}}, [update]);
    return (
        <Box className='options-container' sx={{marginY: margY}}>
                {heading==""?<></>:<p className="options-heading">{heading}</p>}

                <FormGroup row sx={{padding:'.6rem'}}>
                    {options.map(e => {
                        return (
                            <FormControlLabel key={uuid()} control={<Checkbox value={e} checked={checkedItems[e] || false} onChange={() => handleChange(e)} icon={<RadioButtonUncheckedRoundedIcon />} checkedIcon={<CheckCircleRoundedIcon />} />}
                                label={<span style={{ fontSize: fSize }}>{ e}</span>} />
                        )
                    })}
                </FormGroup>       
        </Box>

    )
}