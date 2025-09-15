<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TaskController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\SkillController;

require base_path('routes/api.php');

Route::get('/', function () {
    return view('home');
});
Route::get('/skills', [SkillController::class, 'suggest']);
Route::post('/plan', [SkillController::class, 'generatePlan']);
Route::get('/tasks', [TaskController::class, 'index']);
Route::post('/register', [AuthController::class, 'register'])->name('register');
Route::post('/login', [AuthController::class, 'login'])->name('login');
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');
