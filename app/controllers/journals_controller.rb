class JournalsController < ApplicationController
  before_action :redirect_not_admin, only: [:index, :edit, :update,
                                            :new, :create, :destroy]

  def index
    @journals = Journal.all
  end

  def show
  end

  def edit
  end

  def update
  end

  def new
  end

  def create
  end

  def destroy
  end
end