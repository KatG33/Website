import logo from './logo.svg';
// The line below imports style sheet for App.js
import './App.css';
// The line below imports the main React library, 
// enabling method to use React’s features to create components.
import React from 'react';
// The next FlashcardList component imports a component that supposed to display all the flashcards. 
// It can be done by using command <FlashcardList />
import FlashcardList from './components/FlashcardList';

function App() {
  return (
    <div className="App">
      <FlashcardList />
    </div>
  );
}
export default App;
