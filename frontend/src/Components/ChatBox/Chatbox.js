function Chatbox() {
  return (
    <div className="container">
      <h1>Chat</h1>
      <h2>Your Client Id: </h2>
      <div className="chat-container">
        <div className="chat"></div>
        <div className="my-message">
          <p className="client">client id: </p>
          <p className="message">hello</p>
          <div className="another message containter">
            <div className="another-message"></div>
          </div>
        </div>
      </div>
      <div className="input-chat-container">
        <input
          className="input-chat"
          type="text"
          placeholder="Type your message here"
        />
        <button className="submit-chat">Send</button>
      </div>
    </div>
  );
}

export default Chatbox;
