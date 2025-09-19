<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\TaskController;
use App\Http\Controllers\FileController;

Route::post('/files/upload', [FileController::class, 'upload']);
Route::get('/files/{filename}', [FileController::class, 'download']);
Route::delete('/files/{filename}', [FileController::class, 'delete']);
Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);
Route::post('/logout', [AuthController::class, 'logout']);
Route::get('/tasks', [TaskController::class, 'index']);
