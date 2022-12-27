import * as React from 'react';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import DetailsIcon from '@mui/icons-material/Details';

function Task(props) {
  const [checked, setChecked] = React.useState([]);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

        return (
          <ListItem
            component="span" sx={{ p: 3, border: '1px solid grey' }}
            key={props.value}
            secondaryAction={
              <IconButton edge="end" aria-label="comments">
                <DetailsIcon /> {props.value.priority}
              </IconButton>
            }
            disablePadding
          >
            <ListItemButton role={undefined} onClick={handleToggle(props.value)} dense>
              <ListItemIcon>
                <Checkbox
                  edge="start"
                  checked={checked.indexOf(props.value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{ 'aria-labelledby': props.labelId }}
                />
              </ListItemIcon>
              <ListItemText id={props.labelId} primary={`${props.value.content}`} />
            </ListItemButton>
          </ListItem>
        );
}

export default Task;