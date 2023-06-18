interface FormProps {
  setLevel: any;
  setRole: any;
  setLanguage: any;
  onSubmit: any;
  isLoading: boolean;
}

const Form: React.FC<FormProps> = (props) => {
  return (
    <>
      <div className="my-3">
        <label
          className="block mb-2 text-sm font-medium text-white dark:text-white"
          htmlFor="level-select"
        >
          レベルを選んでください
        </label>
        <select
          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          name="level"
          id="level-select"
          onChange={(e) => props.setLevel(e.currentTarget.value)}
        >
          <option value="Beginner">簡単</option>
          <option value="Intermediate">普通</option>
          <option value="Challenging">高度</option>
        </select>
      </div>
      <div className="my-3">
        <label
          className="block mb-2 text-sm font-medium text-white dark:text-white"
          htmlFor="role-select"
        >
          役割を選んでください
        </label>
        <select
          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          name="role"
          id="role-select"
          onChange={(e) => props.setRole(e.currentTarget.value)}
        >
          <option value="Frontend">Frontend</option>
          <option value="Backend">Backend</option>
          <option value="Fullstack">Fullstack</option>
          <option value="ML">ML</option>
          <option value="Data">Data Engineer</option>
          <option value="Database">Database Developer</option>
          <option value="DevOps">DevOps Engineer</option>
          <option value="QA">QA Engineer</option>
          <option value="Security">Security Engineer</option>
          <option value="Cloud Architect">Cloud Architect</option>
          <option value="IOS Mobile Developer">IOS Developer</option>
          <option value="Android Mobile Developer">Android Developer</option>
          <option value="Web3">Web3</option>
        </select>
      </div>
      <div className="my-3">
        <label
          className="block mb-2 text-sm font-medium text-white dark:text-white"
          htmlFor="language-select"
        >
          言語を選んでください
        </label>
        <select
          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          name="language"
          id="language-select"
          onChange={(e) => props.setLanguage(e.currentTarget.value)}
        >
          <option value="Python">Python</option>
          <option value="JavaScript">JavaScript</option>
          <option value="C">C</option>
          <option value="C++">C++</option>
          <option value="C#">C#</option>
          <option value="R">R</option>
          <option value="Visual Basic">Visual Basic</option>
          <option value="Java">Java</option>
          <option value="PHP">PHP</option>
          <option value="SQL">SQL</option>
          <option value="Go">Go</option>
          <option value="Ruby">Ruby</option>
          <option value="Swift">Swift</option>
          <option value="Dart">Dart</option>
          <option value="Rust">Rust</option>
          <option value="Kotlin">Kotlin</option>
          <option value="Perl">Perl</option>
          <option value="Solidity">Solidity</option>
          <option value="Elixir">Elixir</option>
        </select>
      </div>
      <button
        className="mt-3 w-full bg-gradient-to-r from-teal-400 
        to-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        onClick={props.onSubmit}
        disabled={props.isLoading}
      >
        送信
      </button>
    </>
  );
};

export default Form;