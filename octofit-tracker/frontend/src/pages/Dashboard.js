import React from 'react';

function Dashboard() {
  return (
    <div className="container mt-5">
      <h2>Dashboard</h2>
      <div className="row">
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Activities</h5>
              <p className="card-text">Log your fitness activities here.</p>
              <a href="#" className="btn btn-primary">View Activities</a>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Teams</h5>
              <p className="card-text">Join or create teams.</p>
              <a href="#" className="btn btn-primary">View Teams</a>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Leaderboard</h5>
              <p className="card-text">See how you rank!</p>
              <a href="#" className="btn btn-primary">View Leaderboard</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;