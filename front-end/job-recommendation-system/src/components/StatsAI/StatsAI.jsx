import './StatsAI.css';
import AiButton from '../AiButton/AiButton';
export default function StatsAI({value}) {
    return (
        <div className="StatsAIContainer">
            <AiButton value={value} />
        </div>
    )
}