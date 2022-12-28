import { Button } from "@mui/material";
import Box from "@mui/material/Box";
import Input from "@mui/material/Input";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";

function Chatbox() {
  return (
    <Box sx={{ height: 700 }}>
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
        <FormControl>
          <InputLabel htmlFor="my-input">Type your message here</InputLabel>
          <Input id="my-input" aria-describedby="my-helper-text" />
          <Button variant="contained">Send</Button>
        </FormControl>
      </div>
    </Box>
  );
}

export default Chatbox;
