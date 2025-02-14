import React,{useState} from "react";

function Interest() {
    const [principal, setPrincipal] =useState('')
    const [rate ,setRate] = useState('')
    const[time, setTime] = useState('')
    const[type, setType] = useState('simple')
    const[result,setResult] = useState(null)

    const calculateInterest = () => {
        const p = parseFloat(principal);
        const r = parseFloat(rate) / 100;
        const t = parseFloat(time);

        if (isNaN(p) || isNaN(r) || isNaN(t)) {
            setResult('Please enter valid numbers');
            return;
        }
        
        let interest;
        if (type === 'simple') {
            interest = p * r * t;
        } else if (type === 'compound') {
            interest = p * Math.pow((1 + r), t) - p;
        }

        setResult(interest.toFixed(2));
    }

    return (
        <div>
            <h2>Interest Calculator</h2>
            <div>
                <label>Principal:</label>
                <input type="text" value={principal} onChange={(e) => setPrincipal(e.target.value)} />
            </div>
            <div>
                <label>Rate (%):</label>
                <input type="text" value={rate} onChange={(e) => setRate(e.target.value)} />
            </div>
            <div>
                <label>Time (years):</label>
                <input type="text" value={time} onChange={(e) => setTime(e.target.value)} />
            </div>
            <div>
                <label>Type:</label>
                <select value={type} onChange={(e) => setType(e.target.value)}>
                    <option value="simple">Simple</option>
                    <option value="compound">Compound</option>
                </select>
            </div>
            <button onClick={calculateInterest}>Calculate</button>
            {result !== null && <div>Result: {result}</div>}
        </div>
    );
}

export default Interest;