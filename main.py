#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import better_exceptions
import matplotlib.pyplot as plt
import torch

from cli_options import args
from compress import compress
from model import fake_model, real_model
from plot import plot
from train import train

REAL_EPOCHS = 3
FAKE_EPOCHS = 1 * REAL_EPOCHS

ITERS = 5
# Set seed
torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)

# Don't plot interactively
plt.ioff()

kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}

for iter in range(ITERS):

    # Train
    # real_losses = train(real_model, real=True)
    # fake_losses = train(fake_model, real=False)
    real_losses = train(real_model, real=True, epochs=REAL_EPOCHS)
    fake_losses = train(fake_model, real=False, epochs=FAKE_EPOCHS)

    # Plot performance
    plt = plot(real_losses, fake_losses)
    plt.savefig(f'./figs/{iter}.png')
    plt.gcf().clear()

    # Compress and repeat
    compress(real_model)
    compress(fake_model)
