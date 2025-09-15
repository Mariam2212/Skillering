<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SkillController extends Controller
{
    public function suggest()
    {
        // Run Python and get output
        $output = shell_exec("python3 " . base_path('python/main.py'));
        $data = json_decode($output, true);

        return response()->json($data);
    }

    public function generatePlan(Request $request)
    {
        $skill = $request->input('skill');
        $level = $request->input('level', 'Beginner');

        $command = "python3 " . base_path("python/generate_plan.py") . " \"$skill\" \"$level\"";
        $output = shell_exec($command);

        $data = json_decode($output, true);
        return response()->json($data);
    }
}
