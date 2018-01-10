#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

import torch

# Training settings
parser = argparse.ArgumentParser(description='PyTorch MNIST')

parser.add_argument(
    '--batch-size',
    type=int,
    default=64,
    metavar='N',
    help='input batch size for training (default: 64)',
)

parser.add_argument(
    '--test-batch-size',
    type=int,
    default=1000,
    metavar='N',
    help='input batch size for testing (default: 1000)',
)

parser.add_argument(
    '--epochs',
    type=int,
    default=10,
    metavar='N',
    help='number of epochs to train (default: 10)',
)

parser.add_argument(
    '--lr',
    type=float,
    default=0.01,
    metavar='LR',
    help='learning rate (default: 0.01)',
)

parser.add_argument(
    '--momentum',
    type=float,
    default=0.9,
    metavar='M',
    help='SGD momentum (default: 0.9)',
)

parser.add_argument(
    '--no-cuda',
    action='store_true',
    default=False,
    help='disables CUDA training',
)

parser.add_argument(
    '--seed',
    type=int,
    default=1,
    metavar='S',
    help='random seed (default: 1)',
)

parser.add_argument(
    '--log-interval',
    type=int,
    default=10,
    metavar='N',
    help='how many batches to wait before logging training status',
)

args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()

if __name__ == '__main__':
    pass
