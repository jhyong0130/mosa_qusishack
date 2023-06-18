"use client";
import React, { useState } from "react";
import Form from "./form";
import Results from "./results";

const QusisHack: React.FC = () => {
  const ENDPOINT: string = "https://zcu7ht9al7.execute-api.ap-northeast-1.amazonaws.com/prod/generate_project_ideas";
  const [level, setLevel] = React.useState("");
  const [role, setRole] = React.useState("");
  const [projects, setProjects] = React.useState([]);
  const [hasResult, setHasResult] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(false);

  const onSubmit = () => {
    setIsLoading(true);
    fetch(`${ENDPOINT}?level_input=${level}&role_input=${role}`)
      .then((res) => res.json())
      .then(onResult);
  };

  const onResult = (data: any) => {
    setProjects(data.portfolio_ideas);
    setHasResult(true);
    setIsLoading(false);
  };

  const onReset = (data: any) => {
    setLevel("");
    setRole("");
    setHasResult(false);
    setIsLoading(false);
  };

  let displayedElement = null;

  if (hasResult) {
    displayedElement = <Results projects={projects} onBack={onReset} />;
  } else {
    displayedElement = (
      <Form
        setLevel={setLevel}
        setRole={setRole}
        onSubmit={onSubmit}
        isLoading={isLoading}
      ></Form>
    );
  }

  return (
    <>
      <h1>Qusis Hack</h1>
      {displayedElement}
    </>
  );
};

export default QusisHack;