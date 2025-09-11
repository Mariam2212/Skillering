<?php

namespace App\Http\Middleware;

use Illuminate\Auth\Middleware\Authenticate as Middleware;

class Authenticate extends Middleware
{
    /**
     * Get the path the user should be redirected to when they are not authenticated.
     */
    protected function redirectTo($request): ?string
    {
        // If the request expects JSON, we don't redirect (API behavior)
        if (! $request->expectsJson()) {
            return route('login'); // Change this if your login route is different
        }

        return null;
    }
}
