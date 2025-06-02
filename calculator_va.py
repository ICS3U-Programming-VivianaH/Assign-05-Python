#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: may, 2025
# The program calculates velocity and acceleration


# def the velocity function
def calculate_velocity(distance, time):
    velocity = [0] * 3  # For a list with 3 zeros
    for counter in range(3):
        # Formula
        velocity[counter] = distance[counter] / time[counter]
    return velocity


# def the acceleration function
def calculate_acceleration(velocity, time):
    acceleration = [0] * 3  # For a list with 3 zeros
    for counter in range(3):
        # Formula
        acceleration[counter] = velocity[counter] / time[counter]
    return acceleration


# main function
def main():
    # welcome message
    print("Hello, today this program shall calculate average speed and acceleration")

    # 3 space lists
    distance = [0] * 3
    time = [0] * 3

    # Input distance values
    for counter in range(3):
        while True:
            try:
                # get d
                d = float(input(f"Enter d{counter} value (km): "))
                if d < 0:  # so d is positive
                    print("Distance cannot be negative")
                    continue
                distance[counter] = d
                break
            except ValueError:  # so d is a integer
                print("Please enter a valid number")

    # Input time values
    for counter in range(3):
        while True:
            try:
                # get t
                t = float(input(f"Enter t{counter} value (hours): "))
                if t <= 0:  # so t is positive
                    print("Time must be positive")
                    continue
                time[counter] = t
                break
            except ValueError:  # so d is a integer
                print("Please enter a valid number")

    # Calculations calling the functions
    velocity = calculate_velocity(distance, time)
    acceleration = calculate_acceleration(velocity, time)

    # Display results
    print("\nResults:")
    for i in range(3):  # i is like another counter
        print(f"Measurement {i}:")
        print(f"  Distance: {distance[i]} km")
        print(f"  Time: {time[i]} hours")
        print(f"  Velocity: {velocity[i]:.2f} km/h")
        print(f"  Acceleration: {acceleration[i]:.2f} km/h²")


# end of the main

if __name__ == "__main__":
    main()
