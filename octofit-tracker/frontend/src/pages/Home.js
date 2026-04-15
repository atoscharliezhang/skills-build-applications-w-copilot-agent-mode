import React from 'react';

function Home() {
  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-8 offset-md-2 text-center">
          <h1>Welcome to OctoFit Tracker</h1>
          <p className="lead">Track your fitness activities, join teams, and compete on the leaderboard!</p>
          <img src="/docs/octofitapp-small.png" alt="OctoFit Logo" className="img-fluid mt-4" />
        </div>
      </div>
    </div>
  );
}

export default Home;