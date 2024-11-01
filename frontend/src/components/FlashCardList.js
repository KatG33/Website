// The import 'useEffect' will run the code and load the components, it does things like fetching data from a server. 
// 'useState' will create and manage pieces of data in components, for example, if we wanted to keep track of flashcards, 'useState' could store them
import React, { useEffect, useState } from 'react';
// 'import axios' is a library that sends requests to server to get or send data
import axios from 'axios';
// Funtion that will get and display list of flashcards from one of APIs
function FlashcardList() {
    // Line below initialises a variable called 'flashcards' as an empty list
    // Later on setFlashcards will be used to update 'flashcards'
    const [flashcards, setFlashcards] = useState([]);
    // 'useEffect' function runs when components load for the first time
    useEffect(() => {
        // This sends a request to the server to fetch the flashcards 
        axios.get('http://127.0.0.1:8000/flashcards/api/flashcards/')
            // Once request has succedded the data is saved as 'response.data', then use call 'setFlashcards' to save the data in 'flashcards'
            .then(response => {
                setFlashcards(response.data);
            })
            .catch(error => {
                // If error occurred, comman 'console.error(error)' shows the error in the console
                console.error(error);
            });
    // The empty array [] means the code inside runs only once, when components are created
    }, []); 

    // !!THE PART BELOW SUPPOSED TO RENDER THE UI; It defines what will be shown to the user
    // It is going through and displaying each of our flashcards: 1. Creating unordered list 
    // 2. Each flashcard in the list, item <li> shows a question and corresponding answer
    // 3. Then we use 'key={flashcard.id}' to create a unique key, so React can keep a track of items during each rendering
    return (
        <div>
            <h1>Flashcards</h1> {/* Title */}
            <ul>
                {flashcards.map(flashcard => (
                    <li key={flashcard.id}>
                        <strong>Question:</strong> {flashcard.question} <br />
                        <strong>Answer:</strong> {flashcard.answer}
                    </li>
                ))}
            </ul>
        </div>
    );
}

// Makes ' FlashcardList' component available to other folders
export default FlashcardList;