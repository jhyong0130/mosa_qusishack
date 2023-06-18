interface FormProps {
    setLevel: any;
    setRole: any;
    onSubmit: any;
    isLoading: boolean;
  }
  
  const Form: React.FC<FormProps> = (props) => {
    return (
      <>
        <div>
          <label htmlFor="level-select">レベルを選んでください</label>
          <select
            name="level"
            id="level-select"
            onChange={(e) => props.setLevel(e.currentTarget.value)}
          >
            <option value="Easy">簡単</option>
            <option value="Intermediate">普通</option>
            <option value="Difficult">高度</option>
          </select>
        </div>
        <div>
          <label htmlFor="role-select">役割を選んでください</label>
          <select
            name="role"
            id="role-select"
            onChange={(e) => props.setRole(e.currentTarget.value)}
          >
            <option value="Frontend">Frontend</option>
            <option value="Backend">Backend</option>
            <option value="Fullstack">Fullstack</option>
          </select>
        </div>
        <button onClick={props.onSubmit} disabled={props.isLoading}>
          送信
        </button>
      </>
    );
  };
  
  export default Form;