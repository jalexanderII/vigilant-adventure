import * as React from "react";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

const card = (
  <React.Fragment>
    <CardContent>
      <Typography sx={{ fontSize: 19 }} color="text.secondary" gutterBottom>
        Personal Timer
      </Typography>
      <Typography variant="h5" component="div">
        00:00:00
      </Typography>
    </CardContent>
    <CardActions>
      <Button size="small">start</Button>
      <Button size="small">pause</Button>
    </CardActions>
  </React.Fragment>
);

export default function OutlinedCard() {
  return (
    <Box
      sx={{
        bgcolor: "background.paper",
        boxShadow: 2,
        borderRadius: 2,
        p: 2,
        width: 340,
      }}>
      <Card variant="outlined">{card}</Card>
    </Box>
  );
}
