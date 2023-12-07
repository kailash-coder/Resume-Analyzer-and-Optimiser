/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import axios from "axios";

function Analysis() {
  const [pdfDocs, setPdfDocs] = useState(null);
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const handleFileChange = (e) => {
    setPdfDocs(e.target.files);
  };

  const handleStart = async () => {
    setError("");
    setSummary("");

    if (!pdfDocs) {
      setError("Please upload a valid file.");
      return;
    }

    const formData = new FormData();
    for (const pdfDoc of pdfDocs) {
      formData.append("pdf_docs", pdfDoc);
    }

    try {
      setLoading(true);
      setProgress(30);
      const response = await axios.post(
        "http://127.0.0.1:5000/summarize",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round(
              (progressEvent.loaded * 60) / progressEvent.total
            );
            setProgress(percentCompleted);
          },
        }
      );

      setSummary(response.data.summary);
      setProgress(100);
    } catch (err) {
      setError("An error occurred while processing the document.");
      console.error(err);
    } finally {
      setLoading(false);
      setProgress(0);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[0E0021]">
      <div className="p-8 rounded shadow-md max-w-5xl w-full bg-white">
        <h1 className="text-2xl font-semibold mb-4">Resume Analyzer</h1>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-600">
            Your Resume (PDF)
          </label>
          <input
            type="file"
            accept=".pdf"
            multiple
            onChange={handleFileChange}
            className="mt-1 p-2 border border-gray-300 rounded w-full"
          />
        </div>
        <button
          onClick={handleStart}
          className="bg-[#560043] text-white px-4 py-2 border-[1.5px] border-[#0a0909] border-solid rounded-2xl"
        >
          Start
        </button>
        {error && <p className="text-red-500 mt-4">{error}</p>}
        {loading && (
          <div className="mt-3">
            <p>Loading Progress: {progress}%</p>
            <progress className="w-full" value={progress} max="100" />
          </div>
        )}
        {summary && (
          <div className="mt-5">
            <p className="text-lg font-semibold mb-2">Summary:</p>
            <div className="summary-content">
              {summary.split("\n").map((paragraph, index) => (
                <p key={index} className="mb-2">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Analysis;
