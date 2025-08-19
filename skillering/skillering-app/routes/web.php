<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TaskController; 

Route::get('/', function () {
    return view('home'); 
});

Route::get('/tasks', [TaskController::class, 'index']);
