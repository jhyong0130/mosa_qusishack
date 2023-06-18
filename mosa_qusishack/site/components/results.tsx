interface ResultsProps {
    projects: string[];
    onBack: any;
  }
  
  const Results: React.FC<ResultsProps> = (props) => {
    const projectElements = [];
    for (let i = 0; i < props.projects.length; i++) {
        const element = (<div key={i}>{props.projects[i]}</div>);
        projectElements.push(element);
    }
  
    return (
      <div>
        結果です
        <div>Project: {projectElements}</div>
        <button onClick={props.onBack}>戻る</button>
      </div>
    );
  };
  
  export default Results;