using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Day1
{
    public static string INPUT_FILE 
    { 
        get 
        {
            // Try current directory first (for dotnet run from project folder or tests)
            if (File.Exists("day1.txt"))
                return "day1.txt";
            // Try 2025 subfolder (for dotnet run from workspace root)
            if (File.Exists("2025/day1.txt"))
                return "2025/day1.txt";
            // Fallback
            return "day1.txt";
        }
    }
    public const int START_POINT = 50;
    
    public static readonly string[] EXAMPLE_DATA = {
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    };

    public static IEnumerable<string> ReadData(string filename)
    {
        return File.ReadLines(filename).Select(line => line.Trim());
    }

    public static (char direction, int value) ParseEntry(string entry)
    {
        char direction = entry[0];
        int value = int.Parse(entry.Substring(1));
        return (direction, value);
    }

    public static int ComputeNextPosition(int currentPosition, char direction, int value)
    {
        if (direction == 'L')
        {
            value = ((value / 100) + 1) * 100 - value;
        }

        currentPosition = currentPosition + value;
        currentPosition = currentPosition % 100;

        return currentPosition;
    }

    public static (int position, int countZero) ComputeNextPositionAndNumberZero(int currentPosition, char direction, int value)
    {
        int countZero = 0;
        if (direction == 'L')
        {
            value = -value;
        }

        currentPosition = (currentPosition + value) % 100;

        if (currentPosition < 0)
        {
            currentPosition += 100;
        }   

        countZero += currentPosition / 100;

        if (currentPosition == 0)
        {
            countZero += 1;
        }
        if (value > 0 && currentPosition < (value % 100) && currentPosition != 0)
        {
            countZero += 1;
        }
        if (value < 0 && currentPosition > 100 - (Math.Abs(value) % 100))
        {
            countZero += 1;
        }

        countZero += Math.Abs(value) / 100;

        return (currentPosition, countZero);
    }

    public static int ExampleExercise1()
    {
        int countZero = 0;
        int currentPosition = 50;
        foreach (string entry in EXAMPLE_DATA)
        {
            var (direction, value) = ParseEntry(entry);
            currentPosition = ComputeNextPosition(currentPosition, direction, value);
            if (currentPosition == 0)
            {
                countZero += 1;
            }
        }

        Console.WriteLine($"Count of zero part 1 (example): {countZero}");
        return countZero;
    }

    public static int Exercise1()
    {
        int countZero = 0;
        int currentPosition = START_POINT;
        foreach (string entry in ReadData(INPUT_FILE))
        {
            var (direction, value) = ParseEntry(entry);
            currentPosition = ComputeNextPosition(currentPosition, direction, value);
            if (currentPosition == 0)
            {
                countZero += 1;
            }
        }

        Console.WriteLine($"Count of zero part 1: {countZero}");
        return countZero;
    }

    public static int ExampleExercise2()
    {
        int countZero = 0;
        int currentPosition = START_POINT;
        foreach (string entry in EXAMPLE_DATA)
        {
            var (direction, value) = ParseEntry(entry);
            var (newPosition, addZero) = ComputeNextPositionAndNumberZero(currentPosition, direction, value);
            currentPosition = newPosition;
            countZero += addZero;
        }

        Console.WriteLine($"Count of zero part 2 (example): {countZero}");
        return countZero;
    }

    public static int Exercise2()
    {
        int countZero = 0;
        int currentPosition = START_POINT;
        foreach (string entry in ReadData(INPUT_FILE))
        {
            var (direction, value) = ParseEntry(entry);
            var (newPosition, addZero) = ComputeNextPositionAndNumberZero(currentPosition, direction, value);
            currentPosition = newPosition;
            countZero += addZero;
        }

        Console.WriteLine($"Count of zero part 2: {countZero}");
        return countZero;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Day1.ExampleExercise1();
        Day1.Exercise1();
        Day1.ExampleExercise2();
        Day1.Exercise2();
    }
}
