import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="header">
        <h1>Welcome to My Page</h1>
      </header>
      <main>
        <section className="section">
          <h2>About Me</h2>
          <p>My name is Abhi Ahir. I am from a small country called Panama. I was born and raised there. I am currently in my second semester at CSUSB, having transferred from Chaffey last year. 
          I am trilingual, I know fluently Spanish, English, Hindi, and I used to know French, but forgot it. In my free time, I like playing video games. Also, like playing soccer. 
          I still play mostly three times a week.</p>
        </section>
        <section className="section">
          <div>
            <h3>Hobbies</h3>
            <ul>
              <li>Watching soccer (Favorite Team Barcelona)</li>
              <li>Listening to music</li>
            </ul>
          </div>
          <div>
            <h3>Favorite Activities</h3>
            <ul>
              <li>Going to the gym</li>
              <li>Spending time with family and friends</li>
              <li>Playing soccer</li>
            </ul>
          </div>
          <div>
            <h3>Places I Want to Visit</h3>
            <ul>
              <li>Spain</li>
              <li>Brazil</li>
            </ul>
          </div>
        </section>
        <section className="section">
          <h2>My Image</h2>
          <div className="image-container">
          <img src="https://wallpaper.dog/large/10876668.jpg" alt="Beautiful Landscape" />

          </div>
        </section>
      </main>
      <footer lassName="footer">
        <p>Connect with me on <a href="https://github.com/AbhiFS/Platform-Computing/tree/main/Platform-Computing">GitHub</a></p>
      </footer>
    </div>
  );
}

export default App;
