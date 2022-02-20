{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/matonima/leetcode_questions/blob/main/meeting%20room%202.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#meeting room required minimum for a list of start and end times for meeting\n",
        "def minroom(x):\n",
        "    room=1\n",
        "    for i in range(len(x)):\n",
        "        #j=i+1\n",
        "        for j in range(1,len(x)):\n",
        "            print(\"cheecking if meeting\",x[i], \"clashes with\",x[0])\n",
        "            y=checkroomval(x[j],x[i],room)\n",
        "    return y\n",
        "\n",
        "def checkroomval(x,x0,r):\n",
        "    room=r\n",
        "    start_time=x0[0]\n",
        "    end_time=x0[1]\n",
        "    if x[0]>=start_time and x[1]<=end_time:\n",
        "        print(\"clash in meeting time\")\n",
        "        room=room+1\n",
        "    elif x[0]>start_time and x[1]<end_time:\n",
        "        print(\"clashing times\")\n",
        "        room=room+1\n",
        "    else:\n",
        "        print(\"no clash\")\n",
        "        room=room\n",
        "    return room\n",
        "\n",
        "#drive\n",
        "#x=list[start times, end times]\n",
        "X=[[\"3:00\",\"4:00\"],[\"1:30\",\"2:30\"],[\"2:00\",\"3:00\"],[\"5:00\",\"7:00\"]]\n",
        "print(\"No of rooms needed\", minroom(X))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f5CwVdHG-71f",
        "outputId": "ecb8ac65-5db3-41e5-fe86-58c1521340fa"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cheecking if meeting ['3:00', '4:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['3:00', '4:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['3:00', '4:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['1:30', '2:30'] clashes with ['3:00', '4:00']\n",
            "clash in meeting time\n",
            "cheecking if meeting ['1:30', '2:30'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['1:30', '2:30'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['2:00', '3:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['2:00', '3:00'] clashes with ['3:00', '4:00']\n",
            "clash in meeting time\n",
            "cheecking if meeting ['2:00', '3:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['5:00', '7:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['5:00', '7:00'] clashes with ['3:00', '4:00']\n",
            "no clash\n",
            "cheecking if meeting ['5:00', '7:00'] clashes with ['3:00', '4:00']\n",
            "clash in meeting time\n",
            "No of rooms needed 2\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOYW7WI7gLRMi6a0E1QaKq7",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}