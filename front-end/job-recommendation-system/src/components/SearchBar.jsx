import './SearchBar.css';
import { InputAdornment, TextField } from "@mui/material";
import { useState } from "react";
import SearchIcon from "@mui/icons-material/Search";
export default function SearchBar({toSearch, searchHeight=50, searchColor="white", onSearch=null}) {
    const [searchTerm, setSearchTerm] = useState("");

    const handleChange = (event) => {
        //function for realtime searchvalue change
        setSearchTerm(event.target.value);
        {onSearch===null?{}:onSearch(searchTerm)}
    };
    return (

        <TextField
            id="search"
            className='search'
            type="search"
            placeholder={toSearch}
            value={searchTerm}
            onChange={handleChange}
            InputProps={{
                sx: { borderRadius: 30 ,height: searchHeight, backgroundColor: searchColor},
                endAdornment: (
                    <InputAdornment position="end">
                        <SearchIcon />
                    </InputAdornment>
                ),
            }}
        />

    )
}