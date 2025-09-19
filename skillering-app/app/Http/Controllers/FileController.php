<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class FileController extends Controller
{
    // POST /files/upload
     public function upload(Request $request)
    {
        $request->validate([
            'file' => 'required|file|max:5120' // 5MB limit
        ]);

        $path = $request->file('file')->store('uploads');

        return response()->json([
            'message' => 'File uploaded successfully',
            'filename' => basename($path),
            'path' => $path
        ]);
    }

    // GET /files/{filename}
    public function download($filename)
    {
        if (Storage::exists("uploads/$filename")) {
            return Storage::download("uploads/$filename");
        }

        return response()->json(['error' => 'File not found'], 404);
    }

    // DELETE /files/{filename}
    public function delete($filename)
    {
        if (Storage::exists("uploads/$filename")) {
            Storage::delete("uploads/$filename");
            return response()->json(['message' => 'File deleted successfully']);
        }

        return response()->json(['error' => 'File not found'], 404);
    }
}

