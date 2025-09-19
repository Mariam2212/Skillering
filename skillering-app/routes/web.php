<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TaskController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\SkillController;

require base_path('routes/api.php');

Route::get('/skills', [SkillController::class, 'suggest']);
Route::post('/plan', [SkillController::class, 'generatePlan']);
Route::get('/tasks', [TaskController::class, 'index']);
Route::post('/register', [AuthController::class, 'register'])->name('register');
Route::post('/login', [AuthController::class, 'login'])->name('login');
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

// Home
Route::get('/', function () {
    return view('welcomepage.welcomepage');
})->name('welcomepage');

// Sign In / Sign Up
Route::get('/signin', function () {
    return view('sign_in.sign_in');
})->name('signin');

Route::get('/signup', function () {
    return view('sign_up.sign_up');
})->name('signup');

// Forget Password
Route::get('/forget-password', function () {
    return view('forgetpassword.forgetpassword');
})->name('forgetpassword');

// Verify
Route::get('/verify', function () {
    return view('verify.verify');
})->name('verify');

Route::get('/verify/cant-access-email', function () {
    return view('verify.cant_access_this_email');
})->name('cant_access_email');

// Welcome pages
Route::get('/welcome', function () {
    return view('welcomepage.welcomepage');
})->name('welcome');

Route::get('/dashboard', function () {
    return view('welcomepage.dashbord');
})->name('dashboard');

// Suggest page
Route::get('/suggest', function () {
    return view('suggest_page.suggest');
})->name('suggest');

// CSV page
Route::get('/csv', function () {
    return view('csv_page.csv');
})->name('csv');

// Sign Up extra pages
Route::get('/user-agreement', function () {
    return view('sign_up.user_agreement');
})->name('user_agreement');

Route::get('/privacy-policy', function () {
    return view('sign_up.privacy_policy');
})->name('privacy_policy');

Route::get('/cookie-policy', function () {
    return view('sign_up.cookie_policy');
})->name('cookie_policy');

Route::get('/send-feedback', function () {
    return view('sign_up.send_feedback');
})->name('send_feedback');

Route::get('/terms-conditions', function () {
    return view('sign_up.terms_of_conditions');
})->name('terms_conditions');
