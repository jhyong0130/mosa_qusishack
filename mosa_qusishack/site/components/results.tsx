interface ResultsProps {
  jobs: string;
  projects: string[];
  tutorials: string[];
onBack: any;
}

const Results: React.FC<ResultsProps> = (props) => {
const projectElements = [];
for (let i = 0; i < props.projects.length; i++) {
    const element = (<div key={i}>{props.projects[i]}</div>);
    projectElements.push(element);
}
  
    const tutorialElements = [];
    for (let i = 0; i < props.tutorials.length; i++) {
      const element = <div key={i}>{props.tutorials[i]}</div>;
      tutorialElements.push(element);
    }

return (
  <div>
    <div className="my-3">
      <p className="text-lg text-teal-100">
        JOB DESCRIPTION AND SKILLS YOU NEED:
      </p>
      {props.jobs}
    </div>
    <div className="my-3">
      <p className="text-lg text-teal-100">PROJECT YOU CAN TRY: </p>
      {projectElements}
    </div>
    <div className="my-3">
      <p className="text-lg text-teal-100">TUTORIALS: </p> {tutorialElements}
    </div>
    <button
      className="mt-3 w-full bg-gradient-to-r from-teal-400 
      to-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
      onClick={props.onBack}
    >
      戻る
    </button>
  </div>
);
};

export default Results;