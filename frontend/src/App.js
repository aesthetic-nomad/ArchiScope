import React from 'react';
import MapView from './components/MapView';
import UploadForm from './components/UploadForm';

const App = () => (
  <div>
    <h1>ArchiScope</h1>
    <UploadForm />
    <MapView />
  </div>
);

export default App;
