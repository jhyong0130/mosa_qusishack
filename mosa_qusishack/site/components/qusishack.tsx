"use client";
import React, { useState } from "react";
import Form from "./form";
import Results from "./results";
import Image from "next/image";
import logo from "../public/QUSIS_LOGO_Color_Yoko_A.png";

const QusisHack: React.FC = () => {
  const ENDPOINT: string = "https://zcu7ht9al7.execute-api.ap-northeast-1.amazonaws.com/prod";
  const JOB: string = "/generate_jobscope_and_skills";
  const PROJECT: string = "/generate_project_ideas";
  const TUTORIAL: string = "/generate_tutorial_links";

  const [level, setLevel] = React.useState("");
  const [role, setRole] = React.useState("");
  const [language, setLanguage] = React.useState("");
  const [jobs, setJobs] = React.useState("");
  const [projects, setProjects] = React.useState([]);
  const [tutorials, setTutorials] = React.useState([]);
  const [hasResult, setHasResult] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(false);

    const onSubmit = () => {
    setIsLoading(true);
    fetch(`${ENDPOINT + JOB}?role_input=${role}`)
      .then((res) => res.json())
      .then(onJobResult);
    fetch(`${ENDPOINT + TUTORIAL}?language_input=${language}`)
      .then((res) => res.json())
      .then(onTutorialResult);
    fetch(
      `${
        ENDPOINT + PROJECT
      }?level_input=${level}&language_input=${language}&role_input=${role}`
    )
      .then((res) => res.json())
      .then(onProjectResult);
  };

  const onJobResult = (data: any) => {
    setJobs(data.job_scope_and_skills_required);
    setHasResult(true);
    setIsLoading(false);
  };

  const onProjectResult = (data: any) => {
    setProjects(data.portfolio_ideas);
    setHasResult(true);
    setIsLoading(false);
  };

  const onTutorialResult = (data: any) => {
    setTutorials(data.tutorial_links);
    setHasResult(true);
    setIsLoading(false);
  };

  const onReset = (data: any) => {
    setLevel("");
      setRole("");
      setLanguage("");
    setHasResult(false);
    setIsLoading(false);
  };

  let displayedElement = null;

  if (hasResult) {
    displayedElement = (
      <Results
        projects={projects}
        tutorials={tutorials}
        jobs={jobs}
        onBack={onReset}
      />
    );
  } else {
    displayedElement = (
      <Form
        setLevel={setLevel}
        setRole={setRole}
        setLanguage={setLanguage}
        onSubmit={onSubmit}
        isLoading={isLoading}
      ></Form>
    );
  }

  return (
    <div className="h-screen flex">
      <div className="max-w-md m-auto p-2">
        <div className="bg-gray-700 p-6 rounded-md text-white">
          <div className="text-center my-6">
            <Image src={logo} alt="Qusis Logo" width={400} height={400} />
            <h1 className="text-5xl text-white font-light mt-3">Qusis Hack</h1>
          </div>
          {displayedElement}
        </div>
      </div>
    </div>
  );
};

export default QusisHack;