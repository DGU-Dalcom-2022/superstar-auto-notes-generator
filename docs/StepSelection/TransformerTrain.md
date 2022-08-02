# Transformer Training 과정

# train.py

epoch loop

train_dataloader

    optimize_parameters()

    display_freq마다

        - evaluate_parameters()

        - save_result

    print_freq마다

        - evaluate_parameters()

        - get_current_losses

        - get_current_metrics

update_learning_rate()

# transformer_model.py

optimize_parameters()

    - set_requires_grad

    - forward

    - backward
    
        tensor의 backward 이용

# base_model.py

set_requires_grad : 해당 신경망의 requires_grad 설정

forward : pass

# transformer/Models.py

forward 